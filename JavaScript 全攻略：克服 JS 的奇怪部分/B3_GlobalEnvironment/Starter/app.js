
b();
console.log('before: ' + a)

var a = 'hello world'

console.log('after: ' + a)

function b () {
	console.log('called b!')
}

// ------------------
// > called b!
// > undefiend
