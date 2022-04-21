드론 호버링 테스트 소프트웨어를 위한 TCP 통신 테스트 코드 입니다.
TCPTestServer.py, TCPTestClient.py 두 파일로 이루어져 있습니다.

개발하신 소프트웨어 테스트용으로는 TCPTestClient.py 파일 사용하시면 되고,
TCP 서버와 클라이언트간에 통신이 어떤 식으로 작동 되는지 시뮬레이션 해 보실 수 있게 간단한 Server 코드도 첨부하였습니다.
TCPTestClient의 경우 실행하시게 되면 프롬프트에 IP 주소와 포트를 입력하게 되어 있습니다.

ex)
Server Address: 192.168.1.76
Server PORT: 23000

이런식으로 입력하시면 됩니다.
서버와 통신에 성공하게 되면 
ENTER u d r l, ctrl + c to quit:
이런 메세지를 확인하실 수 있습니다.
u 로 up, d로 down, r로 right, l로 left 명령을 전달할 수 있습니다.

ctrl+c를 입력하시면 프로그램은 종료되고 TCP 통신 또한 종료됩니다.