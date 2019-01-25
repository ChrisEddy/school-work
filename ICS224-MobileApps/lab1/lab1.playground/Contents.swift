import Foundation
var str = "Hello playground there is a dude named myself Hello there" // sample string
var splitStr = str.components(separatedBy: " ") // seperate string into array
var strDict:[String:Int] = [:] // create empty dictionary
for i in splitStr.enumerated(){ // loop through string array
    var count = strDict[i.element] // assign element to temp variable for later use
    count = count == nil ? 1 : count! + 1 // increment value, if its nil, make it 1
    strDict.updateValue(count!, forKey: i.element) // update dictionary key with new count
}
print(strDict) // print dictionary
