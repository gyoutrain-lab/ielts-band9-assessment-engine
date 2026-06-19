import re

class Band9GradingEngine:
    def __init__(self):
        # Target Band 9 components for evaluation
        self.adverbs = ["clinically", "methodologically", "operationally", "strategically", 
                        "systematically", "pedagogically", "technically", "consequently", "procedurally"]
        
        self.nominal_suffixes = [r"\w+tion\b", r"\w+ment\b", r"\w+ity\b", r"\w+ance\b", r"\w+ence\b"]
        
        self.power_verbs = ["mitigate", "mitigates", "facilitate", "facilitates", "augment", "augments", 
                            "delineate", "delineates", "precipitate", "precipitates", "optimize", "optimizes", 
                            "eliminate", "eliminates", "ensure", "ensures", "recalibrate", "recalibrates"]
        
        self.forbidden_verbs = ["make", "makes", "do", "does", "get", "gets", "show", "shows", "help", "helps", "stop", "stops"]

        # Mock Test Database mapping School English to target competencies
        self.test_items = [
            {
                "id": 1,
                "domain": "Curriculum / Training",
                "school_prompt": "I systematically teach the nurses so they can work better.",
                "hint": "Start with 'Pedagogically', turn 'teach' into 'systematization', and replace 'work better' with a power verb like 'accelerates'."
            },
            {
                "id": 2,
                "domain": "National Patient Safety Goals (NPSG)",
                "school_prompt": "You must clearly follow the safety goals to stop mistakes.",
                "hint": "Start with 'Technically' or 'Systematically', nominalize 'follow' into 'implementation/adherence', and use 'mitigate' or 'eliminate'."
            },
            {
                "id": 3,
                "domain": "Global Labor Transfer (SCFHS/STR)",
                "school_prompt": "The nurses get the certificate when they change their study style.",
                "hint": "Start with 'Methodologically', change 'get the certificate' to 'attainment of licensure', and use 'necessitates' or 'facilitates'."
            },
            {
                "id": 4,
                "domain": "Medication Safety / Reporting",
                "school_prompt": "Checking the patient's ID stops the wrong medication.",
                "hint": "Start with 'Procedurally', turn 'checking' into 'verification', and change 'stops' to 'eliminates' or 'prevents'."
            },
            {
                "id": 5,
                "domain": "Clinical Documentation",
                "school_prompt": "I make a report to show how the nurses do their jobs.",
                "hint": "Start with 'Operationally', convert 'make a report' to 'the compilation of reports', and replace 'show' with 'delineates'."
            }
        ]

    def evaluate_response(self, user_input):
        score = 0
        feedback = []
        cleaned_input = user_input.strip().lower()
        words = cleaned_input.split()

        if not words:
            return 0, ["No input provided."]

        # 1. Evaluate Thematic Fronting (Adverb Hook)
        first_word = words[0].replace(",", "")
        if first_word in self.adverbs and "," in user_input.split()[0]:
            score += 25
            feedback.append("✅ Excellent: Correct use of Adverbial Fronting modifier.")
        else:
            feedback.append("❌ Deficit: Missing an opening structural Adverb followed by a comma (e.g., 'Clinically,').")

        # 2. Evaluate Nominalization Core
        nominal_found = False
        for pattern in self.nominal_suffixes:
            if re.search(pattern, cleaned_input):
                nominal_found = True
                break
        if nominal_found:
            score += 25
            feedback.append("✅ Excellent: Abstract nominalized noun structure verified.")
        else:
            feedback.append("❌ Deficit: Missing a high-weight nominalized subject structure ending in -tion, -ment, -ity, or -ance.")

        # 3. Evaluate Power Verb Engine
        verb_score = 25
        used_power_verb = any(verb in cleaned_input for verb in self.power_verbs)
        used_forbidden_verb = any(r"\b" + verb + r"\b" in cleaned_input for verb in self.forbidden_verbs)

        if used_power_verb:
            if used_forbidden_verb:
                verb_score -= 10
                feedback.append("⚠️ Warning: Detected high-precision verbs, but low-level school verbs (make/do/get) are still present.")
            else:
                feedback.append("✅ Excellent: Strong, audit-grade professional verb deployment.")
        else:
            verb_score = 0
            feedback.append("❌ Deficit: Relies entirely on basic school-level action verbs. Inject precision verbs (e.g., 'mitigates', 'optimizes').")
        score += max(0, verb_score)

        # 4. Evaluate Complex Structure & Vocabulary Density
        if len(words) >= 12 and len(set(words)) / len(words) > 0.7:
            score += 25
            feedback.append("✅ Excellent: High lexical density and complex clause synthesis achieved.")
        else:
            score += 10
            feedback.append("⚠️ Structural note: Sentence length or structural complexity is slightly restricted for Band 9 standards.")

        return score, feedback

    def calculate_band_equivalent(self, percentage):
        if percentage >= 90: return "Band 9.0 (Expert Systemic Register)"
        elif percentage >= 75: return "Band 8.0 - 8.5 (Advanced Professional)"
        elif percentage >= 60: return "Band 7.0 - 7.5 (Operational Competency)"
        else: return "Band 5.0 - 6.5 (School-Level / Transitional English)"

    def run_mock_test(self):
        print("="*70)
        print("   IELTS BAND 9 MIGRATION ENGINE - CLINICAL CURRICULUM TESTING TOOL")
        print("="*70)
        print("Instruction: Transform the raw 'School English' prompts into an authoritative,")
        print("nominalized, and fronted Band 9 utterance.\n")

        total_score = 0
        
        for item in self.test_items:
            print(f"\n[Test Item {item['id']}/{len(self.test_items)}] Domain: {item['domain']}")
            print(f"❌ School Real Baseline: \"{item['school_prompt']}\"")
            print(f"💡 Pedagogical Hint    : {item['hint']}")
            
            user_ans = input("✍️ Enter your Band 9 translation: ")
            
            score, feedback = self.evaluate_response(user_ans)
            total_score += score
            
            print(f"\n--- Evaluation Score: {score}% ---")
            for line in feedback:
                print(line)
            print("-" * 40)

        final_percentage = total_score / len(self.test_items)
        band_rating = self.calculate_band_equivalent(final_percentage)
        
        print("\n" + "="*70)
        print("                      FINAL ASSESSMENT REPORT")
        print("="*70)
        print(f"Aggregated Compliance Accuracy: {final_percentage:.1f}%")
        print(f"Assessed Target Proficiency   : {band_rating}")
        print("="*70)
        print("Assessment sequence complete. Deploy this configuration for your certification pipelines.\n")

if __name__ == "__main__":
    engine = Band9GradingEngine()
    engine.run_mock_test()
