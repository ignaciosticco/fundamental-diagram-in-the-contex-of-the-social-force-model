function[]=pasillo3()

close;

N=10;

fp = fopen('flux_model.dat','w');

for alpha=-5:0.001:20,
A=(1+4*alpha)*eye(N);
B=diag(-2*alpha*ones(1,N-1),1);
C=diag(-2*alpha*ones(1,N-1),-1);

T=A+B+C;
T(1,1)=1+3*alpha;
T(N,N)=1+2*alpha;              % alternative v_{i+1}=v_{i}

D=ones(N,1);

V=T\D;

if alpha<0, J=1; 
else J=(1+0.10*alpha)*mean(V);
end

fprintf(fp,"%f %f\n",alpha,J);
end

fclose(fp);

return;


