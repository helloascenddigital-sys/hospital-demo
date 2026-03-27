import re

original_cards = """
                <!-- Dept 1 -->
                <div class="card animate-on-scroll fade-up" style="padding: 0; overflow: hidden;">
                    <img src="images/gen_medicine.png" alt="General Medicine" style="width: 100%; height: 200px; object-fit: cover;">
                    <div style="padding: 25px; text-align: center;">
                        <div style="display: flex; justify-content: center; margin-top: -55px; position: relative;">
                            <div class="icon-wrap bg-primary-light" style="background: white; border: 4px solid var(--color-bg-light); box-shadow: var(--shadow-sm);">
                                <i class="fas fa-heartbeat"></i>
                            </div>
                        </div>
                        <h3>General Medicine</h3>
                        <p style="font-size: 1rem;">Diagnosis and treatment of adult diseases. Our general physicians
                            provide preventive care and
                            manage chronic conditions like diabetes and hypertension.</p>
                    </div>
                </div>

                <!-- Dept 2 -->
                <div class="card animate-on-scroll fade-up delay-100" style="padding: 0; overflow: hidden;">
                    <img src="images/orthopaedics.png" alt="Orthopaedics" style="width: 100%; height: 200px; object-fit: cover;">
                    <div style="padding: 25px; text-align: center;">
                        <div style="display: flex; justify-content: center; margin-top: -55px; position: relative;">
                            <div class="icon-wrap bg-secondary-light" style="background: white; border: 4px solid var(--color-bg-light); box-shadow: var(--shadow-sm);">
                                <i class="fas fa-bone text-secondary"></i>
                            </div>
                        </div>
                        <h3>Orthopaedics</h3>
                        <p style="font-size: 1rem;">Expert care for musculoskeletal issues. Services include trauma care,
                            joint replacements, and
                            management of sports injuries and fractures.</p>
                    </div>
                </div>

                <!-- Dept 3 -->
                <div class="card animate-on-scroll fade-up delay-200" style="padding: 0; overflow: hidden;">
                    <img src="images/neurology.png" alt="Neurology" style="width: 100%; height: 200px; object-fit: cover;">
                    <div style="padding: 25px; text-align: center;">
                        <div style="display: flex; justify-content: center; margin-top: -55px; position: relative;">
                            <div class="icon-wrap bg-primary-light" style="background: white; border: 4px solid var(--color-bg-light); box-shadow: var(--shadow-sm);">
                                <i class="fas fa-brain"></i>
                            </div>
                        </div>
                        <h3>Neurology</h3>
                        <p style="font-size: 1rem;">Specialized treatment for disorders of the nervous system, including
                            stroke management, epilepsy,
                            and headaches.</p>
                    </div>
                </div>

                <!-- Dept 4 -->
                <div class="card animate-on-scroll fade-up delay-300" style="padding: 0; overflow: hidden;">
                    <img src="images/emergency.png" alt="Emergency & Critical Care" style="width: 100%; height: 200px; object-fit: cover;">
                    <div style="padding: 25px; text-align: center;">
                        <div style="display: flex; justify-content: center; margin-top: -55px; position: relative;">
                            <div class="icon-wrap bg-danger-light" style="background: white; border: 4px solid var(--color-bg-light); box-shadow: var(--shadow-sm);">
                                <i class="fas fa-user-injured"></i>
                            </div>
                        </div>
                        <h3>Emergency & Critical Care</h3>
                        <p style="font-size: 1rem;">24/7 dedicated unit for handling medical emergencies, trauma cases, and
                            critical patient support
                            with advanced life safety systems.</p>
                    </div>
                </div>

                <!-- Dept 5 -->
                <div class="card animate-on-scroll fade-up" style="padding: 0; overflow: hidden;">
                    <img src="images/pediatrics.png" alt="Pediatrics" style="width: 100%; height: 200px; object-fit: cover;">
                    <div style="padding: 25px; text-align: center;">
                        <div style="display: flex; justify-content: center; margin-top: -55px; position: relative;">
                            <div class="icon-wrap bg-secondary-light" style="background: white; border: 4px solid var(--color-bg-light); box-shadow: var(--shadow-sm);">
                                <i class="fas fa-baby text-accent"></i>
                            </div>
                        </div>
                        <h3>Pediatrics</h3>
                        <p style="font-size: 1rem;">Compassionate care for infants, children, and adolescents. Vaccinations,
                            growth monitoring, and
                            treatment of childhood illnesses.</p>
                    </div>
                </div>

                <!-- Dept 6 -->
                <div class="card animate-on-scroll fade-up delay-100" style="padding: 0; overflow: hidden;">
                    <img src="images/gynecology.png" alt="Gynecology" style="width: 100%; height: 200px; object-fit: cover;">
                    <div style="padding: 25px; text-align: center;">
                        <div style="display: flex; justify-content: center; margin-top: -55px; position: relative;">
                            <div class="icon-wrap bg-primary-light" style="background: white; border: 4px solid var(--color-bg-light); box-shadow: var(--shadow-sm);">
                                <i class="fas fa-female text-secondary-dark"></i>
                            </div>
                        </div>
                        <h3>Gynecology</h3>
                        <p style="font-size: 1rem;">Women's health services including maternity care, high-risk pregnancy
                            management, and
                            reproductive health solutions.</p>
                    </div>
                </div>

                <!-- Dept 7 -->
                <div class="card animate-on-scroll fade-up delay-200" style="padding: 0; overflow: hidden;">
                    <img src="images/diagnostics.png" alt="Diagnostics & Labs" style="width: 100%; height: 200px; object-fit: cover;">
                    <div style="padding: 25px; text-align: center;">
                        <div style="display: flex; justify-content: center; margin-top: -55px; position: relative;">
                            <div class="icon-wrap bg-primary-light" style="background: white; border: 4px solid var(--color-bg-light); box-shadow: var(--shadow-sm);">
                                <i class="fas fa-x-ray"></i>
                            </div>
                        </div>
                        <h3>Diagnostics & Labs</h3>
                        <p style="font-size: 1rem;">Advanced diagnostic services including X-Ray, Ultrasound, and full-range
                            pathology laboratory
                            tests available round the clock.</p>
                    </div>
                </div>

                <!-- Dept 8 -->
                <div class="card animate-on-scroll fade-up delay-300" style="padding: 0; overflow: hidden;">
                    <img src="images/pulmonology.png" alt="Pulmonology" style="width: 100%; height: 200px; object-fit: cover;">
                    <div style="padding: 25px; text-align: center;">
                        <div style="display: flex; justify-content: center; margin-top: -55px; position: relative;">
                            <div class="icon-wrap bg-secondary-light" style="background: white; border: 4px solid var(--color-bg-light); box-shadow: var(--shadow-sm);">
                                <i class="fas fa-lungs text-secondary"></i>
                            </div>
                        </div>
                        <h3>Pulmonology</h3>
                        <p style="font-size: 1rem;">Treatment for respiratory conditions such as asthma, COPD, and
                            pneumonia, with critical care
                            support.</p>
                    </div>
                </div>
"""

with open('departments.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace from <!-- Dept 1 --> to the end of <!-- Dept 8 --> div
start_marker = "<!-- Dept 1 -->"
# We know the grid ends with </div>\n            </div>\n        </div>\n    </section>"
# Let's just use regex to replace `<div class="grid" ...>` content
pattern = re.compile(r'(<div class="grid" style="grid-template-columns: repeat\(auto-fit, minmax\(300px, 1fr\)\); gap: 30px;">).*?(</div>\s*</div>\s*</section>)', re.DOTALL)
new_text = pattern.sub(r'\1\n' + original_cards + r'\n            \2', text)

with open('departments.html', 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Saved correctly!")
