let obj = {x: 1, y: 2, z: 3};

for (let el in obj) {
  obj[el] = obj[el] ** 2;
}

console.log(obj); 
