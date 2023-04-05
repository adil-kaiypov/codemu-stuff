const today = new Date();
const date = {
  year: today.getFullYear(),
  month: today.getMonth() + 1,
  day: today.getDate()
};

console.log(`${date.year}-${date.month}-${date.day}`);
