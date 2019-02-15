// Author: Chris Eddy
#include <iostream>
#include <iomanip>
#include <fstream>
#include <math.h>
#include <string>
using namespace std;

void printHeader(ostream &outStream){  // print the first 2 lines of the report
    outStream << right << setw(10) << "deg";
    outStream << setw(10) << "rad";
    outStream << setw(10) << "sin";
    outStream << setw(10) << "cos" << endl;
    outStream << setw(10) << "------";
    outStream << setw(10) << "------";
    outStream << setw(10) << "------";
    outStream << setw(10) << "------" << endl;
}

void printEntry(ostream &outStream, string value){  // print a data row
    double degree = atof(value.c_str());
    outStream << right << setw(10) << fixed << setprecision(1) << degree;
    outStream << setw(10) << setprecision(4) << degree*((atan(1)*4)/180);
    outStream << setw(10) << setprecision(4) << sin (degree*(atan(1)*4)/180);
    outStream << setw(10) << setprecision(4) << cos (degree*(atan(1)*4)/180.0 ) << endl;
} 

int main(int argc, char *argv[]){
    string inputFile;
    string line;
    string outputFile;

    if(argc > 1){
        inputFile = argv[1];
    }
    else{
        inputFile = "default.txt";
    }

    outputFile = "result_" + inputFile;
    ifstream inputStream (inputFile);
    
    if(inputStream.is_open()){
        ofstream outputStream (outputFile);
        if (outputStream.is_open()){
            printHeader(outputStream);
            printHeader(cout);
            while (getline (inputStream, line)){
                printEntry(outputStream, line);
                printEntry(cout, line);
            }
            inputStream.close();
            outputStream.close();
        }
        else{
            cout << "Unable to open output file: " << outputFile;
        } 
    }
    else{
        cout << "Error could not open file: " << inputFile << "\n"; 
    } 

    return 0;
}