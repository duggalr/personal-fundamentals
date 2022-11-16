const { expect } = require('chai');

// Load compiled artifacts
const Box = artifacts.require('SimpleStorage');

// Start test block
contract('SimpleStorage', function () {
  beforeEach(async function () {
    // Deploy a new Box contract for each test
    this.box = await Box.new();
  });

  // Test case
  it('retrieve returns a value previously stored', async function () {
    // Store a value
    await this.box.set(42);

    // Test if the returned value is the same one
    // Note that we need to use strings to compare the 256 bit integers
    expect((await this.box.get()).toString()).to.equal('42');
  });
});


