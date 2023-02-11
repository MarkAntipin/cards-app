function creteRandomValue(from, to, step) {
  return  Math.floor(Math.random() * Math.floor((to - from) / step)) * step + from
}

export {creteRandomValue}
