# hoveringController
# hovering controller drone test center
UI for Ipad 9th generation to adjust gps coordinate to test drone hovering.
Through TCP connection it sends the data to adjust the coordinate for the drone.


<img width="853" alt="스크린샷 2022-02-21 오후 10 28 13" src="https://user-images.githubusercontent.com/54619996/160056869-35dd077e-5820-4029-a7f5-3433c033720f.png">

- you can create TCP socket connetion to the server.
- you can send socket containing (1, 0), (-1, 0), (0, 1), (0, -1) corresponding to each right, left, up and down.
- The server will reply the updated coordinate with latitude and longitude. It will be displayed on the screen.
