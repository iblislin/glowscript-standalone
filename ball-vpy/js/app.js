const options = {
  lang: 'vpython',
  version: 2.1
};

window.__context = {
  glowscript_container: $('#glowscript'),
};

const execute = function (code) {
  const js_code = glowscript_compile(code, options);
  const program = eval(js_code);
  
  console.log(js_code);
  program(function(err){
    console.log(err)
  });
}

const fetch_code = function(url){
  fetch(url)
    .then(function(res){
      return res.text();
    })
    .then(execute);
}

fetch_code('./py/ball.py')
