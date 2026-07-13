const chat = document.getElementById("chat");

const input = document.getElementById("message");

const button = document.getElementById("send");

function addMessage(text, cls){

const div=document.createElement("div");

div.className=cls;

div.innerText=text;

chat.appendChild(div);

chat.scrollTop=chat.scrollHeight;

}

button.onclick = async ()=>{

const message=input.value.trim();

if(message==="") return;

addMessage(message,"user");

input.value="";

const response=await fetch("http://127.0.0.1:8000/chat",{

method:"POST",

headers:{

"Content-Type":"application/json"

},

body:JSON.stringify({

message:message

})

});

const data=await response.json();

addMessage(data.reply,"bot");

}

input.addEventListener("keydown",(e)=>{

if(e.key==="Enter"){

button.click();

}

});
