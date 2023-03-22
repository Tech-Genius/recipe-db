$(document).ready(function () {
	$(".sm_controls .open").click(function () {


	   $(".sm_controls .open").hide();
	   $(".sm_controls .close").fadeIn();

	   $(".header_inner .menu").slideToggle("500", "swing");
	   //  $(".head_side").css("padding-top", "200px");

	})
 });



 $(document).ready(function () {
	$(".sm_controls .close").click(function () {

	   $(".sm_controls .close").hide();
	   $(".sm_controls .open").fadeIn();

	   $(".header_inner .menu").slideToggle("slow");
	   //  $(".head_side").css("padding-top", "200px");

	})
 });