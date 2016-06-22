var code = 'sphere()'
var options = {
  lang: 'vpython',
  version: 2.1
}
window.__context = {
  glowscript_container: $('#glowscript')
}
eval(glowscript_compile(code, options))(function(err){})
