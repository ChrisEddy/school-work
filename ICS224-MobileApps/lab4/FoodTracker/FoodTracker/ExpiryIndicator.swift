//
//  ExpiryIndicator.swift
//  FoodTracker
//
//  Created by Drake on 2019-02-13.
//  Copyright © 2019 Chris. All rights reserved.
//

import UIKit

class ExpiryIndicator: UIStackView {
    private var indicators = [UIImageView]()
    private let indicatorCount: Int = 10
    var indicatorPercentage: Int = 100{
        didSet{
            for i in 0..<indicatorCount{
                indicators[i].alpha = i * indicatorCount < indicatorPercentage ? 1.0 : 0.1
            }
        }
    }
    
    required init(coder: NSCoder){
        super.init(coder:coder)
        for _ in 0..<self.indicatorCount{
            let indicator = UIImageView(image: #imageLiteral(resourceName: "defaultImage"))
            indicator.contentMode = .scaleToFill
            self.addArrangedSubview(indicator)
            indicators.append(indicator)
        }
    }

    /*
    // Only override draw() if you perform custom drawing.
    // An empty implementation adversely affects performance during animation.
    override func draw(_ rect: CGRect) {
        // Drawing code
    }
    */

}
