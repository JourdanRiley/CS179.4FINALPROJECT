window.onload = function() {
	var d = new Date();
	var month_name = ['January','Februaruy','March','April','May','June','July','August','September','October','November','December'];
	var month = d.getMonth();
	var year = d.getFullYear();
	var first_date = month_name[month] + " " + 1 + " " + year;
	var temp = new Date(first_date).toDateString();
	var first_day = temp.substring(0, 3);
	var day_name = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat'];
	var day_no = day_name.indexOf(first_day);
	var days = new Date(year, month+1, 0).getDate();
	document.getElementById("calendar-month-year").innerHTML = month_name[month] + " " +year;
	getJSON('/holidates/?format=json')
	.then(res=>{
		var calendar = get_calendar(day_no, days, res);
	document.getElementById("calendar-dates").appendChild(calendar);
	})

}

function getJSON(url){
	return new Promise(function(resolve, reject){
		$.get(url, function(data, status){
			resolve(data)
		});
	});
}


function get_calendar(day_no, days, res){
	var d = new Date();
	var table = document.createElement('table');
	var tr = document.createElement('tr');
	
	for(var c=0; c<=6; c++){
		var td = document.createElement('td');
		td.innerHTML = "SMTWTFS"[c];
		tr.appendChild(td);
	}
	table.appendChild(tr);
	
	tr = document.createElement('tr');
	var c;
	for(c=0; c<=6; c++){
		if(c == day_no){
			break;
		}
		var td = document.createElement('td');
		td.innerHTML = "";
		tr.appendChild(td);
	}
	
	var count = 1;
	for(; c <=6; c++){
		var td = document.createElement('td');
		td.innerHTML = count;
		for(var j = 0; j < res.length; j++)
		{
			if(count == res[j].Day)
			{
				td.innerHTML = res[j].Holiday;
				console.log(res[j].Holiday);
			}
		}
		count++;
		if(count == d.getDate() + 1)
		{
			td.style.backgroundColor = 'green';
			tr.appendChild(td);
		}
		tr.appendChild(td);
	}
	table.appendChild(tr);
	
	for(var r=3; r<=6; r++){
		tr = document.createElement('tr');
		for(var c =0;c<=6; c++)
		{
			if(count > days){
				table.appendChild(tr);
				return table;
			}
			var td = document.createElement('td');
			td.innerHTML = count;
		for(var j = 0; j < res.length; j++)
		{
			if(count == res[j].Day)
			{
				td.innerHTML = res[j].Holiday;
				console.log(res[j].Holiday);
			}
		}
			count++;
			if(count == d.getDate() + 1)
			{
				td.style.backgroundColor = 'green';
				tr.appendChild(td);
			}
			tr.appendChild(td);
		}
		table.appendChild(tr);
	}

}

