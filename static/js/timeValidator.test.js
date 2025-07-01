const isValidTimeInterval = require('./timeValidator');

test('returns true for valid 15-minute intervals', () => {
  expect(isValidTimeInterval("10:00")).toBe(true);
  expect(isValidTimeInterval("12:15")).toBe(true);
  expect(isValidTimeInterval("13:30")).toBe(true);
  expect(isValidTimeInterval("15:45")).toBe(true);
});

test('returns false for invalid minutes', () => {
  expect(isValidTimeInterval("10:10")).toBe(false);
  expect(isValidTimeInterval("12:22")).toBe(false);
  expect(isValidTimeInterval("08:59")).toBe(false);
});