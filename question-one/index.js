function findUniqueItems(arr) {
    const seen = new Set();
    const duplicates = new Set();

for (const item of arr) {
    if (seen.has(item)) {
      duplicates.add(item);
    } else {
      seen.add(item);
        }
    }

    return Array.from(seen).filter(item => !duplicates.has(item)).sort((a,b) => a-b);
}


const arr = [1,2,3,4,1,213,78,89,81,23,45,5,6,12,34,56,76,54,12];
console.log(findUniqueItems(arr)); 