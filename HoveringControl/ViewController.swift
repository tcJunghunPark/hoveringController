//
//  ViewController.swift
//  HoveringControl
//
//  Created by Junghun Park on 2022/02/21.
//

import UIKit

class ViewController: UIViewController {
    let cod = coordiViewModel()
    let socket = socketConnection.socket
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        updateCoordinate()
    }

    @IBOutlet weak var coordinate: UILabel!
    
    @IBOutlet var up: UIView!
    @IBOutlet var down: UIView!
    @IBOutlet var left: UIView!
    @IBOutlet var right: UIView!
    
    @IBAction func moveDown(_ sender: Any) {
        cod.newY(-1)
        updateCoordinate()
        socket.sendMessage(msg: cod.msg)
        print("message sent : \(cod.msg)")
        cod.reset()
        
    }
    @IBAction func moveRight(_ sender: Any) {
        cod.newX(1)
        updateCoordinate()
        socket.sendMessage(msg: cod.msg)
        print("message sent : \(cod.msg)")
        cod.reset()
        
    }
    @IBAction func moveUp(_ sender: Any) {
        cod.newY(1)
        updateCoordinate()
        socket.sendMessage(msg: cod.msg)
        print("message sent : \(cod.msg)")
        cod.reset()
        
    }
    @IBAction func moveLeft(_ sender: Any) {
        cod.newX(-1)
        updateCoordinate()
        socket.sendMessage(msg: cod.msg)
        print("message sent : \(cod.msg)")
        cod.reset()
        
    }
    
    func updateCoordinate(){
        coordinate.text = "( \(cod.getX) , \(cod.getY) )"
    }
}
