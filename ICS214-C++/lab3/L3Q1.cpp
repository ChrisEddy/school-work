// Author: Chris Eddy
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main(int argc, char *argv[]){
    string inputFile;
    string line;
    if(argc > 1){
        inputFile = argv[1];
    }
    else{
        inputFile = "default.txt";
    }
    ifstream myfile (inputFile);
    if(myfile.is_open()){
        while (getline (myfile, line)){
            cout << line << '\n';
            writeFile(inputFile, line);
        }
        myfile.close();
    }
    else{
        cout << "Unable to open file" << "\n"; 
    } 
    return 0;
}

int writeFile (string fileName, string data){
    ofstream myfile;
    myfile.open ("result_" + fileName + ".txt");
    if(myfile.is_open()){
        myfile << "Writing this to a file.\n";
        myfile.close();
    }
    else{
        cout << "Unable to open file" << "\n"; 
    } 
    return 0;
}