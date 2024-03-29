#include <unistd.h>
#include <sys/stat.h>
#include <arpa/inet.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAXLINE 1024
#define PORTNUM 3500

int main(int argc, char *argv[]) {
	struct sockaddr_in serveraddr;
	int server_sockfd;
	int client_len;
	int readnn, writenn, writename;
	char buf[MAXLINE];
	char rbuf[MAXLINE];
	pid_t pid;
	
	if(3!=argc){
		fprintf(stderr, "usage: %s <server>\n", argv[0]);
		exit(1);
	}
	printf("server : %s\nname : %s\n", argv[1], argv[2]);

	if ((server_sockfd = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
		perror("error :");
		return 1;
	}

	serveraddr.sin_family = AF_INET;
	serveraddr.sin_addr.s_addr = inet_addr(argv[1]);
	serveraddr.sin_port = htons(PORTNUM);
	client_len = sizeof(serveraddr);

	if (connect(server_sockfd, (struct sockaddr *)&serveraddr, client_len) < 0)
	{
		perror("connect error :");
		return 1;
	}
	else {
		printf("connect success\n");
		// send client name to server
		writename=write(server_sockfd, argv[2], sizeof(argv[2]));
		if(writename<= 0){
			perror("write error : ");
			return 1;
		}
		printf("sending name : %s\n", argv[2]);
	}
	memset(buf, 0x00, MAXLINE); 
	
	pid=fork();
	
	// child process : send message to server
	if(pid ==0){
		printf("I'm child process!, pid : %d\n", pid);
		
		while(1){
			fgets(buf,sizeof(buf),stdin);
			writenn=write(server_sockfd, buf, MAXLINE);
			if(writenn<= 0)
			{
				perror("write error : ");
				return 1;
			}
			printf("sending %s : %s", argv[2], buf);
			
			if(strcmp(buf, "exit\n") == 0){
				exit(1);
			}
		}
		close(server_sockfd);
		return 1;
	}
	// parent process : receive message from server
	else if(pid>0){
		printf("I'm parent process!, pid : %d\n", pid);
		while(1){
			readnn = read(server_sockfd, buf, MAXLINE);
			if(readnn <= 0){
				perror("read() error\n");
				exit(1);
			}
			printf("reading %s : %s",argv[2], buf);
			if(strcmp(buf, "exit\n") == 0){
				exit(1);
			}
		}
		exit(1);
	}
	// close(server_sockfd);
	return 0;
}
