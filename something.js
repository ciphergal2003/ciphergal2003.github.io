const params = new URLSearchParams(window.location.search);
const key = params.get('access-key');

if (key == "aaaaaa"){
  window.location.href = "data.json";
}
