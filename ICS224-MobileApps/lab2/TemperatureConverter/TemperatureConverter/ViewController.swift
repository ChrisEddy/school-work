//
//  ViewController.swift
//  TemperatureConverter
//
//  Created by Drake on 2019-01-28.
//  Copyright © 2019 Drake. All rights reserved.
//

import UIKit

class ViewController: UIViewController, UITextFieldDelegate {
    
    var temperature:Double = 0
    
    // MARK: Properties
    @IBOutlet weak var tempField: UITextField!
    @IBOutlet weak var tempResult: UILabel!
    
    // MARK: DelegateMethods
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        self.tempField.delegate = self
    }
    func textFieldShouldReturn(_textField: UITextField) -> Bool{
        self.tempField.resignFirstResponder()
        return true
    }

    // MARK: Actions
    @IBAction func toF(_ sender: Any) {
        let input:String = self.tempField.text!
        if(isNumeric(a: input)){
            temperature = Double(input)! * 9.0 / 5.0 + 32.0
            self.tempResult.text = String(temperature)
        }
        else{
            self.tempResult.text = "N/A"
        }
    }
    
    @IBAction func toC(_ sender: Any) {
        let input:String = self.tempField.text!
        if(isNumeric(a: input)){
            temperature = Double(input)! * 5.0 / 9.0
            self.tempResult.text = String(temperature)
        }
        else{
            self.tempResult.text = "N/A"
        }
    }
    
    func isNumeric(a: String) -> Bool {
        return Double(a) != nil
    }
}

