// #include <bits/stdc++.h>
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <vector>

using namespace std;

int main(int argc, char **argv) {
  std::vector<std::string> s;
  s.emplace_back("a");
  s.emplace_back("b");
  s.emplace_back("c");
  s.push_back("d");

  cout << s.size() << endl;
  std::cout << s[0] << std::endl;
  std::cout << "Hello World~~~" << std::endl;
  return 0;
}