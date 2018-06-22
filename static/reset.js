//install react module
//const React = require('react')
//const ReactDOM = require('react-dom');



window.onload = function drawGraph(){
    $.ajax({
        url : '/draw_graph',
        type : 'GET',
        dataType : 'json',
        success : function(res){
            alert( res.pet );
/*
            data_num = res.pet.length;
            var label = new Array(data_num);
            var pet_num = new Array(data_num);
            var bin_num = new Array(data_num);
            var can_num = new Array(data_num);
            i = 0;
            for(var item in res.pet){
                pet_num[i] = res.pet[item];
                i++;
            }
            j = 0;
            for(var item in res.bin){
                bin_num[j] = res.bin[item];
                j++
            }
            k = 0;
            for(var item in res.can.item){
                can_num[k] = res.can[item];
                k++;
            }
            $('div').text([res]);*/
        }
    })
} 

/*
var ctx = document.getElementById("myChart").getContext('2d');
var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['A','B','C','D','E','F','G'],
        datasets: [{
            label: 'apples',
            data: [12, 19, 3, 17, 28, 24, 7]
        }, {
            label: 'oranges',
            data: [30, 29, 5, 5, 20, 3, 10]
        }]
    }
});
*/