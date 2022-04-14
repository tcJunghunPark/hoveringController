//
//  UDPViewController.swift
//  HoveringControl
//
//  Created by Junghun Park on 2022/02/21.
//

import UIKit

class UDPViewController: UIViewController {
    
    override func viewDidLoad() {
        super.viewDidLoad()
        connectionMsg.text = ""
    }
    
    @IBOutlet weak var connectionMsg: UILabel!
    @IBOutlet weak var addrText: UITextField!
    
    @IBOutlet weak var portText: UITextField!
    
    @IBAction func connection(_ sender: Any) {
        let socket = socketConnection.socket
        
        guard let addr = addrText.text, addr.isEmpty == false else {return}
        guard let portTxt = portText.text, portTxt.isEmpty == false else {return}
        guard let port = Int32(portTxt) else {return}
        
        socket.changeAddr(addr: addr)
        socket.changePort(port: port)
        socket.initSocket(addr: addr, port: port)
        var connection_state = socket.connect()
        
        if connection_state == 1{
            connectionMsg.text = "connection init!"
        }else{
            connectionMsg.text = "Fail to Connect!"
        }
        
        print("---> address \(addr), port \(port) connected")
    }
}

