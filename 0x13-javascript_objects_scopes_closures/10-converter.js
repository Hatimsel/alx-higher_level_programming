#!/usr/bin/node

exports.converter = function (base) {
  return function (param) {
    return param.toString(base);
  };
};
