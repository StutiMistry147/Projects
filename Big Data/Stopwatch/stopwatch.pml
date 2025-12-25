chan tick = [0] of {bool};
chan sig_S = [1] of {bool};
chan sig_R = [1] of {bool};

bool is_running = false;
int sec_count = 0;
int min_count = 0;

proctype SimulatedInputs(){
	do
	::tick?_ -> 
		atomic{
			if
			::(sec_count==3)->sig_S!true
			::(sec_count==5)->sig_R!true
			::(sec_count==10)->sig_S!true
			::(sec_count==15)->atomic{sig_S!true; sig_R!true}
			::else -> skip
			fi
		}
	od
}
bool S_detected = false;
bool R_detected = false;

proctype ModelLogic(){
	do
	::tick?_ ->
		if
		::S_detected->
			is_running = !is_running;
			S_detected = false
		::else -> skip
		fi
	od
}

inline reset_time(){
	sec_count = 0;
	min_count = 0;
}

proctype RestartLogic(){
	do
	::tick?_ ->
		if
		::R_detected->
			if
			:: S_detected->
				reset_time();
				is_running=true;
				S_detected=false
			::else->
				reset_time();
				is_running=false
			fi;
			R_detected=false
		::else -> skip
		fi
	od
}

proctype Timer(){
	do
	::tick?_->
		if
		::is_running ->
			sec_count++;
			if
			::sec_count>=60->
				sec_count = 0;
				min_count++
			::else->skip
			fi
		::else -> skip
		fi
	od
}

proctype Display(){
	do
	::tick?_ -> 
		if
		::is_running -> 
			printf(">>> Time = %d minute(s), %d second(s)\n", min_count, sec_count);
			printf(">>> MODE = GO\n")
		::else ->
			printf(">>> MODE =STOP\n")
		fi
	od
}

proctype SignalHandler(){
	bool val;
	do
	::tick?_ -> 
		if
		:: sig_S ? [val] -> sig_S ? val; S_detected = true
		:: sig_R ? [val] -> sig_R ? val; R_detected = true
		::else -> skip
		fi
	od
}

#define MAX_TICKS 20
proctype ClockTick(){
	int t=0;
	do
	::t < MAX_TICKS ->
		atomic{
			tick!true; tick!true; tick!true; tick!true; tick!true;
		}
		t++
	::else -> break
	od
}

init{
	atomic{
		run SimulatedInputs();
		run SignalHandler();
		run RestartLogic();
		run ModelLogic();
		run Timer();
		run Display();
		run ClockTick();
	}
}

