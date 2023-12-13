#!/usr/bin/node
exports.esrever = function (list) {
  let a = 0;
  let end = list.length - 1;
  while (a < end) {
    const p = list[a];
    list[a] = list[end];
    list[end] = p;
    a++;
    end--;
  }
  return list;
};
