#!/usr/bin/node
const x = parseInt(process.argv[2]);
function factorial (n) {
  if (n === 'NaN' || n === 1) {
    return 1;
  } else {
    n *= factorial(n - 1);
    console.log(n);
  }
}
factorial(x);
