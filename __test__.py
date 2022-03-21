from camera_control import CameraControl


def example_ptz_zoom(ip, user, password):
    ptz_cam = CameraControl(ip, user, password)
    ptz_cam.camera_start()
    
    # while True:
    # ptz_cam.absolute_move(0.0, 0.0, 1)  # ( Pan, Tilt, Zoom )
    # time.sleep(2)

    # ptz_cam.absolute_move(0.3, 0.1, 1)  # ( Pan, Tilt, Zoom )
    # time.sleep(2)

    # ptz_cam.absolute_move(0.6, 0.5, 1)  # ( Pan, Tilt, Zoom )
    # time.sleep(2)

    # ptz_cam.absolute_move(0.9, 0.8, 1)  # ( Pan, Tilt, Zoom )
    # time.sleep(2)

    # ptz_cam.absolute_move(-0.5, 0.8, 1)  # ( Pan, Tilt, Zoom )
    # time.sleep(2)

    # ptz_cam.go_home_position()

    print("Presets: ", ptz_cam.get_preset())
    print("Presets: ", ptz_cam.get_preset_complete())



example_ptz_zoom("192.168.15.13", "admin", "admin")
