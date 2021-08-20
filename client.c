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
	int readnn, writenn;
	char buf[MAXLINE];
	char rbuf[MAXLINE];
	pid_t pid;
	
	if(3!=argc){
		fprintf(stderr, "usage: %s <server> <ID>\n", argv[0]);
		exit(1);
    }
	printf("%s\n%s\n%s\n", argv[0], argv[1], argv[2]);

	if ((server_sockfd = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
		perror("error :");
		return 1;
	}

	server_sockfd = socket(AF_INET, SOCK_STREAM, 0);
	serveraddr.sin_family = AF_INET;
	serveraddr.sin_addr.s_addr = inet_addr(argv[1]);
	serveraddr.sin_port = htons(PORTNUM);
	client_len = sizeof(serveraddr)

	if (connect(server_sockfd, (struct sockaddr *)&serveraddr, client_len) < 0)
	{
		perror("connect error :");
		return 1;
	}
	else {
		printf("connect success\n");
	}
	memset(buf, 0x00, MAXLINE); 		
		
	pid=fork();
		
	if(pid ==0){
		while(1){
			fgets(buf,sizeof(buf),stdin);
			writenn=write(server_sockfd, buf, MAXLINE);			
			if(writenn<= 0)
			{
				perror("write error : ");
				return 1;
			}
			
			if((strncmp,"exit",4) == 0){
				exit(0);
			}
		}
		exit(0);
	}
	else if(pid>0){
		while(1){
			readnn = read(server_sockfd, buf, MAXLINE);
			if(readnn <= 0){
				perror("read() error\n");
				exit(0);
			}
			printf("%s : %s",argv[2], buf);
			if(strncmp(buf,"exit",4) == 0){
				exit(0);
			}	
		}	
	}	
	close(server_sockfd);
	return 0;
}