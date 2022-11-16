module.exports = async function main (callback) {
  try {

    const Box = artifacts.require('MyToken');
    const box = await Box.deployed();

    const tokenName = await box.name();
    const tokenSymbol = await box.symbol();
    console.log('tokenName/symbol:', tokenName, tokenSymbol);

    const pubKeyAddress = "0x90F8bf6A479f320ead074411a4B0e7944Ea8c9C1";

    // // Mint NFT; TODO: I need the token-ID created for the NFT <-- will keep counter on my end?
    // await box.safeMint(pubKeyAddress, "https://game.example/item-id-8u5h2m.json");
    // console.log('nft-token-id:', nftTokenID);
    // console.log('nft-token-string:', JSON.stringify(nftTokenID) );
    
    const allTokens = await box.getOwnedTokenIds(pubKeyAddress);
    console.log('all-tokens:', allTokens);

    // const tokenSupply = await box.totalSupply();

    // console.log('token-supply:', tokenSupply.toString());

    // // 0xd03ea8624C8C5987235048901fB614fDcA89b117
    // // 0xACa94ef8bD5ffEE41947b4585a84BdA5a3d3DA6E

    
    // const allTokens = await box._ownedTokens[pubKeyAddress];
    // console.log('all-toks:', allTokens);

    // // Get Owner Balance
    // const ownerBalance = await box.balanceOf(pubKeyAddress)
    // console.log('owner-balance:', ownerBalance.toString());

    // const tokenID = 0
    // const ownerAddress = await box.ownerOf(tokenID);
    // console.log('owner-addr:', ownerAddress);

    // const tokenMetaData = await box.tokenURI(tokenID);
    // console.log('token-metadata:', tokenMetaData);

    callback(0);
    
  } catch (error) {
    
    console.error(error);
    callback(1);

  }


}