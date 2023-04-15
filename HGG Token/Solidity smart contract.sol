// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract HGGToken {
    string public name = "HGG Token";
    string public symbol = "HGG";
    uint256 public totalSupply = 1000000 * 10**18; // 1 million HGG

    mapping(address => uint256) public balanceOf;

    constructor() {
        balanceOf[msg.sender] = totalSupply;
    }

    function transfer(address to, uint256 amount) external returns (bool) {
        require(balanceOf[msg.sender] >= amount, "Not enough balance");
        balanceOf[msg.sender] -= amount;
        balanceOf[to] += amount;
        return true;
    }
}
