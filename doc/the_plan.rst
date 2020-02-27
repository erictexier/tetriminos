## to do date

- finish with google_api basic services:  email, drive and notification
- learn more about Blueprint in flask and the use of  url_prefix='/blah'
 (https://flask.palletsprojects.com/en/1.1.x/tutorial/views/)
- use of docker for singularity
 (https://stackoverflow.com/questions/57416579/activate-conda-environment-in-singularity-container-from-dockerfile)
- update dataflow for web code update


navbar css
#navbar {
  background-color: #333;
  position: fixed;
  top: -50px;
  width: 100%;
  display: block;
  transition: top 0.9s;
}

#navbar a {
  float: left;
  display: block;
  color: #f2f2f2;
  text-align: center;
  padding: 15px;
  text-decoration: none;
  font-size: 17px;
}

#navbar a:hover {
  background-color: #ddd;
  color: black;
}
navbar js

window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    document.getElementById("navbar").style.top = "0";
  } else {
    document.getElementById("navbar").style.top = "-50px";
  }
}
navbar html
