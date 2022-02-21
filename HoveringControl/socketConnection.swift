//
//  socketConnection.swift
//  HoveringControl
//
//  Created by Junghun Park on 2022/02/21.
//

import UIKit
import Foundation
import SwiftSocket

public typealias Byte = UInt8

class socketConnection {
    static let socket = socketConnection()
    
    init() {
        self.addr = "127.0.0.1"
        self.port = Int32(8000)
    }
    var addr : String?
    var port : Int32
    var client : UDPClient?
    
    func initSocket (addr : String, port : Int32) {
        self.addr = addr
        self.port = port
        client = UDPClient(address: addr, port: port)
        //connect()
    }
    func sendMessage(msg:String){
        guard let client = client else {return}
        
        switch client.send(string: msg){
        case .success:
            print("\(msg) sent")
        case .failure(let error):
            print("Fail to send, error : \(error)")
        }
    }
    func changeAddr(addr : String){
        self.addr = addr
    }
    func changePort(port : Int32){
        self.port = port
    }
    func broadCast() {
        guard let client = client else {return}
        client.enableBroadcast()
    }
    

}
