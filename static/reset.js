
var label = [];
var pet_num = [];
var bin_num = [];
var can_num = [];

window.onload = function drawGraph(){
    $.ajax({
        url : '/draw_graph',
        type : 'GET',
        dataType : 'json',
        success : function(res){
            //alert(res.pet_amount["2018/4"]); OK
            for(var item in res.pet_amount){
                label.unshift(item);
                pet_num.unshift(res.pet_amount[item]);
            }
            for(var item in res.bin_amount){
                bin_num.unshift(res.bin_amount[item]);
            }
            for(var item in res.can_amount){
                can_num.unshift(res.can_amount[item]);
            }
            dataset = {
                labels: label,
                datasets: [{
                    label: 'PET BOTTLE',
                    data: pet_num
                }, {
                    label: 'BIN',
                    data: bin_num
                },{
                    label: 'CAN',
                    data: can_num
                }]
            }
            
            var ctx = document.getElementById("myChart").getContext('2d');
            var myChart = new Chart(ctx, {
                type: 'line',
                data: dataset
            });
        }
    })

    
    
} 

