def main(): 
	import sys
	global play
	play = True;
	while play == True:
	
		def get_initial_input():
			global quiz, test, labs, assignment
			quiz = int(input("Enter number of quizzes?: "));
			test = int(input("Enter number of tests?: "));
			labs = int(input("Enter number of labs?: "));
			assignment = int(input("Enter number of assignments?: "));

		def prompt_final():
			global final
			final = int(input("Does your final weigh differently than the other tests? (1 = yes, 0 = no): "));

		def get_weights():
			if quiz > 0:
				global quiz_weight
				quiz_weight = int(input("How much do your quizzes weigh?: "));
			else:
				quiz_weight = 0;

			if test > 0:
				global test_weight
				test_weight = int(input("How much do your tests weigh?: "));
			else:
				test_weight = 0;
			if labs > 0:
				global labs_weight
				labs_weight = int(input("How much do your labs weigh?: "));
			else:
				labs_weight = 0;

			if assignment > 0:
				global assignment_weight
				assignment_weight = int(input("How much do your assignments weigh?: "));
			else:
				assignment_weight = 0;

			if final == 1:
				global final_weight
				final_weight = int(input("How much does your final weigh?: "));
			else:
				final_weight = 0;


		def weights_error():
			if quiz_weight + test_weight + labs_weight + assignment_weight + final_weight != 100:
				print("Something went wrong! Your total is not 100%");
				play = False;

		def get_scores():
			global quiz_scores, test_scores, labs_scores, assignment_scores, final_score
			quiz_scores = []
			test_scores = []
			labs_scores = []
			assignment_scores = []
			final_score = []

			for i in range(0, quiz):
				quiz_scores.append(float(input("Enter one of your quiz scores: ")));
			for i in range(0, test):
				test_scores.append(float(input("Enter one of your test scores: ")));
			for i in range(0, labs):
				labs_scores.append(float(input("Enter one of your labs scores: ")));
			for i in range(0, assignment):
				assignment_scores.append(float(input("Enter one of your assignment scores: ")));
			for i in range(0, final):
				final_score.append(float(input("Enter your final score: ")));


		def calculate_weighted_avg():
			global quiz_done, test_done, labs_done, assignment_done, final_done, total_grade
			if quiz > 0:
				quiz_done = (sum(quiz_scores)/len(quiz_scores))/100*quiz_weight
			else:
				quiz_done = 0;
			if test > 0:
				test_done = (sum(test_scores)/len(test_scores))/100*test_weight
			else:
				test_done = 0;

			if labs > 0:
				labs_done = (sum(labs_scores))/100*labs_weight
			else:
				labs_done = 0;

			if assignment > 0:
				assignment_done = (sum(assignment_scores)/len(assignment_scores))/100*assignment_weight
			else:
				assignment_done = 0;
			if final > 0:
				final_done = (sum(final_score)/len(final_score))/100*final_weight
			else:
				final_done = 0;

				total_grade = quiz_done + test_done + labs_done + assignment_done + final_done;


		def print_grade():
			if total_grade >= 90:
				print("Your grade is an A!");
			elif total_grade >= 80:
				print("Your grade is a B!");
			elif total_grade >= 70:
				print("Your grade is a C!");
			elif total_grade >= 60:
				print("Your grade is a D!");
			else:
				print("Your grade is a F!");

		def restart():
			restart = input("Do you want to calculate another grade? (y/n): ");
			if restart == "y":
				play == True;
			else:
				sys.exit()
			
		get_initial_input();
		prompt_final();
		get_weights();
		weights_error();
		get_scores();
		calculate_weighted_avg();
		print_grade();
		restart();

main();
