var vm1 = new Vue({
                el:"#data",
                data:{
                Usedspace:Usedspace+"G",
                capacity:capacity+"G"
                }
                });
if(width>80){
                background="red"
                }else if(width >=60 && width <=80){
                    background="yellow"
                }else if(width <60){
                background="#4CAF50"
                }
var vm2 = new Vue({
                el:"#skills",
                data:{
                TheStyle:{
               width:width+"%",
               background:background
            }
                }
                });

var vm3 = new Vue({
                el:"#data1",
                data:{
                width1:width
                }
                });