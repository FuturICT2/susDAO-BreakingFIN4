pragma solidity 0.4.23;

contract RedirectToMe 
{
    address me = 0xb5bfA9367D67ED0FE738Ae69B80735a3C45D3421;

    function () payable 
    {
        me.send(msg.value);
    }

 }
 
 
 //deployed on rinkeby to 0x81c8989574d0acbebe7d40fd9133ca941415b579
