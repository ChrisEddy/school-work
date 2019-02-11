// Author: Chris Eddy
#include <iostream>
#include <iomanip>
#include <fstream>
#include <math.h>
#include <string>
using namespace std;

void printHeader(ostream &outStream){  // print the first 2 lines of the report
    cout << right << setw(10) << "deg";
    cout << right << setw(10) << "rad";
    cout << right << setw(10) << "sin";
    cout << right << setw(10) << "cos" << endl;
    cout << right << setw(10) << "------";
    cout << right << setw(10) << "------";
    cout << right << setw(10) << "------";
    cout << right << setw(10) << "------" << endl;
    outStream << right << setw(10) << "deg";
    outStream << right << setw(10) << "rad";
    outStream << right << setw(10) << "sin";
    outStream << right << setw(10) << "cos" << endl;
    outStream << right << setw(10) << "------";
    outStream << right << setw(10) << "------";
    outStream << right << setw(10) << "------";
    outStream << right << setw(10) << "------" << endl;
}

void printEntry(ostream &outStream, string value){  // print a data row
    double degree = atof(value.c_str());
    cout << right << setw(10) << setprecision(4) << degree;
    cout << right << setw(10) << setprecision(4) << degree*((atan(1)*4)/180);
    cout << right << setw(10) << setprecision(4) << sin (degree*(atan(1)*4)/180);
    cout << right << setw(10) << setprecision(4) << cos (degree*(atan(1)*4)/180.0 ) << endl;
    outStream << right << setw(10) << degree;
    outStream << right << setw(10) << setprecision(4) << degree*((atan(1)*4)/180);
    outStream << right << setw(10) << setprecision(4) << sin (degree*(atan(1)*4)/180);
    outStream << right << setw(10) << setprecision(4) << cos (degree*(atan(1)*4)/180.0 ) << endl;
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
    ofstream outputStream (outputFile);

    if(inputStream.is_open()){
        if (outputStream.is_open()){
            printHeader(outputStream);
            while (getline (inputStream, line)){
                printEntry(outputStream, line);
            }
            inputStream.close();
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