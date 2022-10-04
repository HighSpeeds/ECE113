t=0:0.001:1;
f_s=10;
for f_0=[3 7 13]
	y=cos(2*pi*f_0*t);
	n=0:1/f_s:1;
	y_sampled=cos(2*pi*f_0*n);
	plot(t,y)
	hold on;
	stem(n,y_sampled)
	title(strcat("f_0=",int2str(f_0)," f_s=",int2str(f_s)))
	xlabel("time (seconds)")
	ylabel("amplitude")
	legend(strcat("cos(2*pi*",int2str(f_0),"*t)"),
		strcat("sampled at f_s=",int2str(f_s)))
	saveas(gcf,strcat("f_0",int2str(f_0),".png"))
	hold off;
end
