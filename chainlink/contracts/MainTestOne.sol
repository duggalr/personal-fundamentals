// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./VRFConsumerV2";



contract MainTestOne {

  VRFConsumerV2 private vrfConsumer;

  constructor(){

    vrfConsumer = VRFConsumerV2(
      6716, 
      0x2Ca8E0C643bDe4C2E08ab1fA0da3401AdAD7734D,
      0x326C977E6efc84E512bB9C30f76E30c160eD06FB,
      0x79d3d8832d904592c0bf9818b621522c988bb8b0c05cdc3b15aea1b6e8db0c15
    );

  //   vrfConsumer.requestRandomWords();

  // tx = vrf_consumer.requestRandomWords()
  //   tx.wait(1)
  //   request_id = tx.events[0]["requestId"]
 
  }



}


// TODO: 
  // start with web-app, and then build contract <-- get basic, localhost version complete (deploy to AWS later in week)
  // generate random from python (it's OS so trust is still there; chainlink-vrf can but not most ideal at the moment...)
    // contract will only be for deposits and rewards
    // **do check if pool-amount > 0 and the amount should be reset 


