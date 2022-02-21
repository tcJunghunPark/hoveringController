//
//  coordinate.swift
//  HoveringControl
//
//  Created by Junghun Park on 2022/02/21.
//

import UIKit

class coordinate{
    static let shared = coordinate()
    var x: Int = 0
    var y: Int = 0
    
    func updateX(x: Int){
        self.x += x
    }
    func updateY(y: Int){
        self.y += y
    }
    func reset(){
        self.x = 0
        self.y = 0
    }
}

class coordiViewModel {
    private let coordi = coordinate.shared
    
    var getX: Int {
        return coordi.x
    }
    var getY: Int {
        return coordi.y
    }
    func newX(_ x: Int){
        coordi.updateX(x: x)
    }
    func newY(_ y: Int){
        coordi.updateY(y: y)
    }
    func reset() -> Void {
        coordi.reset()
    }
}
