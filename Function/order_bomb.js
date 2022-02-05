//Hydrogen bomb
	//remember to correct the date number
	var activityid = '1512';
	jQuery.ajax({
		url:ska.activity_book+'/'+"1512"+'/application',
		type:'GET',
		dateType:'json',
		data:{'id':activityid},
		complete: function(xhr, textStatus) {
		    //called when complete
		  },
		  success: function(data, textStatus, xhr) {
		  	//var rooms = data.data.list;
		  	if(data.status){
		  		alertDialog(data.msg,'success');
		  	}else{
		  		alertDialog(data.msg,'error');
		    	//window.location.reload();
		  	}
			//alert(rooms);
		  	//var leng = childdata.length;
		  },
		  error: function(xhr, textStatus, errorThrown) {
		    //called when there is an error
		    alertDialog('网络错误，请重试','error');
		    window.location.reload();
		  }
	});

//atom bomb
let timerId = setInterval(() => {
    document.getElementById("signUp").click();
	//click"book"
    document.getElementsByName("mobile")[0].value="19200000000";
	//fill phone number
    document.getElementsByClassName("ui-dialog-autofocus")[0].click();
	//click cross if fail
    }, 2000);
