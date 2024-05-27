#include<bits/stdc++.h>

#define read(x) int x;cin>>x

using namespace std;

int generate_random (int a,int b){
	random_device rd;
	default_random_engine generator(rd());
	uniform_int_distribution<int> distribution(a,b);
	int random_number=distribution(generator);
	return random_number;
}

void press_any_key() {
	cin.ignore(numeric_limits<streamsize>::max(),'\n');
}

int main(){
	int r=generate_random(1,6);
	cout<<"**********Welcome to the RUSSIAN ROULETTE**********"<<endl;
	cout<<"Wish you luck cus you might need it :)"<<endl;
	cout<<"The gun is loaded!! Do you want to start?\n1. Yes\n2. No\n>>";
	read(op1);

	bool chance;
	if(op1==1){
		cout<<"You have some real guts huh..."<<endl<<endl;
		chance=true;
	}
	else{
		cout<<"Seems like courage abandoned you at the last moment..."<<endl<<endl;
		chance=false;
	}

    press_any_key();
	for(int i=1;i<=r;i++){
		cout<<"*****Round "<<i<<"*****"<<endl<<endl;
		if(i==r && chance==true){
			cout<<"Its YOUR turn...Press [enter] to trigger"<<endl;
			press_any_key();
			cout<<"[BANG!]...You Died!!";
			press_any_key();
		}
		else if(i==r && chance==false){
            cout<<"Its MY turn...Press [enter] to trigger"<<endl;
			press_any_key();
			cout<<"[BANG!]...I Died!!...You Win!!";
			press_any_key();
		}
		else if(i!=r && chance==true){
			cout<<"Its YOUR turn...Press [enter] to trigger"<<endl;
			press_any_key();
			cout<<"[Click!]...You're Safe"<<endl<<endl;
			chance=false;
		}
		else if(i!=r && chance==false){
			cout<<"Its MY turn...Press [enter] to trigger"<<endl;
			press_any_key();
			cout<<"[Click!]..I'm Safe"<<endl<<endl;
			chance=true;
		}
	}
}