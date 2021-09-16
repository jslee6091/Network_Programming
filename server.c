#include <sys/types.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <signal.h>
#include <stdlib.h>

#define MAXLINE 1024
#define PORTNUM 3500

int main(int argc, char *argv[]) {
	int listen_fd, client_fd;
	pid_t pid;
	socklen_t addrlen;
	int readn, readname;
	int usernumber = 0;
	char* userList[10];
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

	signal(SIGCHLD, SIG_IGN); //to predict zombie process

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
		if(usernumber >= 10){
			char* message = "Number of user is maximum";
			int writeOver = write(client_fd, message, sizeof(message));
			if(writeOver <= 0){
				perror("write error : ");
				return 1;
			}
		}

		// read name of client
		if((readname=read(client_fd, userEnter, sizeof(userEnter)))<=0){
			perror("read error\n");
			exit(1);
		}
		userList[usernumber] = userEnter;
		printf("client name : %s\n", userList[usernumber]); 
		usernumber++;

		pid = fork();

		// child process
		if(pid == 0)
		{
			while(1){
				if((readn=read(client_fd, buf, MAXLINE))<=0){
					perror("read error\n");
					exit(1);
				}

				int writemsg = write(client_fd, buf, MAXLINE);
				if(writemsg <= 0){
					perror("write wrong\n");
					exit(1);
				}
				printf("%s : %s", userList[usernumber - 1], buf);
				if(strcmp(buf, exits) == 0){
					printf("%s is exit\n", userList[usernumber - 1]);
					int writeExit = write(client_fd, exits, sizeof(exits));
					if(writeExit <= 0){
						perror("exit write error\n");
					}
					exit(1);
				}
			}
			close(client_fd);
			usernumber--;
			return 0;
		}
		
	}
	close(listen_fd);
	return 0;
}
