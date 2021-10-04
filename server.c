#include <sys/types.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <signal.h>
#include <stdlib.h>
#include <sys/shm.h>
#include <sys/ipc.h>

#define MAXLINE 1024
#define PORTNUM 3500

struct userinfo{
	int usernumber;
	int client_fd_list[10];
	char userList[10][MAXLINE];
};

int main(int argc, char *argv[]) {
	int listen_fd, client_fd;
	pid_t pid;
	socklen_t addrlen;
	int readn, readname;
	struct userinfo *users;
	void* shared_memory = (void*)0;
	char userEnter[MAXLINE];
	char buf[MAXLINE];
	char exits[] = "exit\n";
	struct sockaddr_in client_addr, server_addr;

	if( (listen_fd = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
		return 1;
	}

	memset((void *)&server_addr, 0x00, sizeof(server_addr));
	server_addr.sin_family = AF_INET;
	server_addr.sin_addr.s_addr = htonl(INADDR_ANY);
	server_addr.sin_port = htons(PORTNUM);

	if(bind(listen_fd, (struct sockaddr *)&server_addr, sizeof(server_addr)) ==-1)
	{
		perror("bind error");
		return 1;
	}
	else{
		printf("bind success\n");
	}

	if(listen(listen_fd, 5) == -1)
	{
		perror("listen error");
		return 1;
	}
	else {
		printf("listen success\n");
	}	

	// predict zombie process
	signal(SIGCHLD, SIG_IGN);

	// make shared memory
	int shmid = shmget((key_t)1234, sizeof(struct userinfo), 0666|IPC_CREAT);

	// attach to the shared memory
	shared_memory = shmat(shmid, (void*)0, 0);
	if(shared_memory == (void*)-1){
		perror("shmat failed : ");
		exit(1);
	}
	printf("shared_memory : %d\n", shared_memory);

	// wrte or read data to shared memory
	users = (struct userinfo*)shared_memory;

	if(shmid == -1){
		perror("shared memory failed : ");
		exit(1);
	}

	memset(buf, 0x00, MAXLINE);
	while(1){
		printf("client waiting\n");
		addrlen = sizeof(client_addr);
		client_fd = accept(listen_fd, (struct sockaddr *)&client_addr, &addrlen);

		if(client_fd == -1)
		{
			printf("accept error\n");
			return 1;
		}
		else{
			printf("accept success\n");
		}

		printf("client accepted!, client_fd : %d\n", client_fd);

		// if user number get over the limit, send message to client
		if(users->usernumber >= 10){
			char* message = "Number of user is maximum";
			int writeOver = write(client_fd, message, sizeof(message));
			if(writeOver <= 0){
				perror("write error : ");
			}
			return -1;
		}

		// read name of client
		if((readname=read(client_fd, userEnter, sizeof(userEnter)))<=0){
			perror("read error\n");
			exit(1);
		}

		// register username and client_socket_number(client_fd)
		users->client_fd_list[users->usernumber] = client_fd;
		strcpy(users->userList[users->usernumber], userEnter);
		users->usernumber++;

		printf("client name : %s\n", users->userList[users->usernumber-1]); 
		printf("client fd : %d\n", users->client_fd_list[users->usernumber-1]); 
		printf("user num : %d\n", users->usernumber);

		// make another process
		pid = fork();

		// child process
		if(pid == 0)
		{
			while(1){
				// read user list from shared memory
				//users = (struct userinfo*)shared_memory;

				printf("============================\n");
				
				// receive message from clients
				if((readn=read(client_fd, buf, MAXLINE))<=0){
					perror("read error\n");
					exit(1);
				}
				printf("received message : %s\n", buf);

				printf("usernumber : %d\n", users->usernumber);

				// write message to other clients
				for(int i = 0; i < users->usernumber; i++){
					printf("client_fd_list[%d] : %d\n", i, users->client_fd_list[i]);
					printf("send message : %s\n", buf);
					int writemsg = write(users->client_fd_list[i], buf, MAXLINE);
					if(writemsg <= 0){
						printf("writemsg : %d\n", writemsg);
						perror("write wrong\n");
						exit(1);
					}
					printf("%s : %s", users->userList[i], buf);
				}

				if(strcmp(buf, exits) == 0){
					printf("%s is exit\n", users->userList[users->usernumber - 1]);
					int writeExit = write(client_fd, exits, sizeof(exits));
					if(writeExit <= 0){
						perror("exit write error\n");
					}
					exit(1);
				}
			}
			close(client_fd);
			printf("socket closed\n");
			users->usernumber--;
			return 0;
		}
		if(shmctl(shmid, IPC_RMID, 0) == -1){
			printf("shared memory remove failed : ");
			return -1;
		}
		else{
			printf("shared memory removed!\n");
		}
	}
	// close shared memory
	/*
	if(shmctl(shmid, IPC_RMID, 0) == -1){
		printf("shared memory remove failed : ");
		return -1;
	}
	else{
		printf("shared memory removed!\n");
	}*/

	close(listen_fd);
	return 0;
}
