pragma solidity ^0.8.0;

contract HelloWorld {
  string greeting = "Merhaba Dunya!";

  function greet() public view returns (string memory) {
    return greeting;
  }

  function setGreeting(string memory _greeting) public {
    greeting = _greeting;
  }
}
