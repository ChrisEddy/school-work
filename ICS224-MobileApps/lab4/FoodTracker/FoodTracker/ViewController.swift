//
//  ViewController.swift
//  FoodTracker
//
//  Created by Drake on 2019-02-13.
//  Copyright © 2019 Chris. All rights reserved.
//

import UIKit
import os

class ViewController: UIViewController, UIImagePickerControllerDelegate, UINavigationControllerDelegate {
    
    // MARK: - Properties
    
    @IBOutlet weak var expiryDate: UIDatePicker!
    @IBOutlet weak var photoImageView: UIImageView!
    @IBOutlet weak var expiryIndicator: ExpiryIndicator!
    
    @IBAction func selectImageFromPhotoLibrary(_ sender: UITapGestureRecognizer) {
        let imagePickerController = UIImagePickerController()
        imagePickerController.sourceType = .photoLibrary
        imagePickerController.delegate = self
        self.present(imagePickerController, animated: true, completion:nil)
    }
    
    func imagePickerControllerDidCancel(_ picker: UIImagePickerController){
        dismiss(animated: true, completion:nil)
    }
    
    func imagePickerController(_ picker: UIImagePickerController, didFinishPickingMediaWithInfo info: [UIImagePickerController.InfoKey : Any]){
        guard let selectedImage = info[UIImagePickerController.InfoKey.originalImage] as?
        UIImage else{
            os_log("Missing image in %@", log: OSLog.default, type: .debug, info)
            return
        }
        photoImageView.image = selectedImage
        dismiss(animated: true, completion: nil)
        
    }
    
    @objc func dateChanged(_ sender: UIDatePicker){
        debugPrint(sender.date)
//        setIndicatorPercentage(sender.date)
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        self.expiryDate.addTarget(self, action: #selector(dateChanged(_:)), for:.valueChanged)
    }
    
//    func setIndicatorPercentage(date: Date()){
//        var date = date
//    }


}

