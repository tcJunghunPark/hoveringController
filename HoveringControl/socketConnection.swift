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
    var client : TCPClient?
    
    func initSocket (addr : String, port : Int32) {
        self.addr = addr
        self.port = port
        client = TCPClient(address: addr, port: port)
        //connect()
    }
    func sendMessage(msg:String) -> String{
        guard let client = client else {return ""}
        
        switch client.connect(timeout: 10){
        case .success:
            print("\(msg) sent")
            let newMsg: String = msg + "\n\n"
            if let response = sendRequest(string: newMsg, using: client){
                return response
            }
        case .failure(let error):
            print("Fail to send, error : \(error)")
//            let errMsg : String = String(describing: error)
            return "-1"
            
        }
        return ""
    }
    private func sendRequest(string: String, using client: TCPClient) -> String? {
        switch client.send(string:string) {
        case .success:
            return readResponse(from: client)
        case .failure(let error):
            let errMsg : String = String(describing: error)
            return errMsg
        }
    }
    private func readResponse(from client: TCPClient) -> String? {
        guard let response = client .read(1024*10) else {return nil}
        print(response)
        return String(bytes: response, encoding: .utf8)
    }
    func changeAddr(addr : String){
        self.addr = addr
    }
    func changePort(port : Int32){
        self.port = port
    }
    public enum SocketError: Error {
        case queryFailed
        case connectionClosed
        case connecitonTimeout
        case unknownError
        
    }
    
    

}
