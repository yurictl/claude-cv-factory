#!/usr/bin/env python3
"""
Universal RenderCV YAML validation script
Supports different validation modes: quick, detailed, and full
"""
import yaml
import sys
import argparse
from rendercv.data import validate_input_dictionary_and_return_the_data_model

def quick_validate(yaml_file):
    """Quick validation - just check if valid"""
    try:
        with open(yaml_file, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        validate_input_dictionary_and_return_the_data_model(data)
        print("✅ Valid")
        return True
    except Exception as e:
        print(f"❌ Invalid: {e}")
        return False

def detailed_validate(yaml_file):
    """Detailed validation with section information"""
    try:
        with open(yaml_file, 'r', encoding='utf-8') as file:
            yaml_content = yaml.safe_load(file)
        
        print(f"📄 Validating file: {yaml_file}")
        print("=" * 50)
        
        data_model = validate_input_dictionary_and_return_the_data_model(yaml_content)
        print("✅ Schema validation PASSED!")
        print()
        
        # Display CV information
        print("📋 CV Information:")
        print(f"   Name: {data_model.cv.name}")
        print()
        
        # Check sections
        sections = data_model.cv.sections
        print("📚 Sections found:")
        
        if hasattr(sections, 'summary') and sections.summary:
            print(f"   ✅ Summary: {len(sections.summary)} items")
        
        if hasattr(sections, 'experience') and sections.experience:
            print(f"   ✅ Experience: {len(sections.experience)} entries")
            for i, exp in enumerate(sections.experience, 1):
                print(f"      {i}. {exp.position} at {exp.company}")
        
        if hasattr(sections, 'education') and sections.education:
            print(f"   ✅ Education: {len(sections.education)} entries")
            for i, edu in enumerate(sections.education, 1):
                print(f"      {i}. {edu.degree} in {edu.area} from {edu.institution}")
        
        if hasattr(sections, 'technical_skills') and sections.technical_skills:
            print(f"   ✅ Technical Skills: {len(sections.technical_skills)} categories")
            for skill in sections.technical_skills:
                print(f"      - {skill.label}: {skill.details}")
        
        if hasattr(sections, 'certifications') and sections.certifications:
            print(f"   ✅ Certifications: {len(sections.certifications)} items")
            for cert in sections.certifications:
                print(f"      - {cert.bullet}")
        
        print()
        print("🎉 All validations passed! Your CV is ready for rendering.")
        return True
        
    except Exception as e:
        print("❌ Schema validation FAILED!")
        print(f"Error: {e}")
        print()
        print("💡 Common issues:")
        print("   - Missing required fields (e.g., 'area' in education)")
        print("   - Incorrect data types")
        print("   - Invalid date formats")
        print("   - Missing section headers")
        return False

def full_validate(yaml_file):
    """Full validation with all possible checks"""
    try:
        with open(yaml_file, 'r', encoding='utf-8') as file:
            yaml_content = yaml.safe_load(file)
        
        print(f"🔍 Full validation of: {yaml_file}")
        print("=" * 60)
        
        # YAML syntax check
        print("1. YAML syntax check... ✅")
        
        # Schema validation
        print("2. Schema validation...")
        data_model = validate_input_dictionary_and_return_the_data_model(yaml_content)
        print("   ✅ Schema validation PASSED!")
        
        # Detailed analysis
        print("3. Content analysis...")
        print(f"   CV Name: {data_model.cv.name}")
        
        sections = data_model.cv.sections
        section_count = 0
        
        if hasattr(sections, 'summary') and sections.summary:
            section_count += 1
            print(f"   ✅ Summary section: {len(sections.summary)} items")
        
        if hasattr(sections, 'experience') and sections.experience:
            section_count += 1
            print(f"   ✅ Experience section: {len(sections.experience)} entries")
            # Check for required fields in experience
            for i, exp in enumerate(sections.experience):
                if not hasattr(exp, 'company') or not exp.company:
                    print(f"   ⚠️  Experience entry {i+1}: Missing company")
                if not hasattr(exp, 'position') or not exp.position:
                    print(f"   ⚠️  Experience entry {i+1}: Missing position")
        
        if hasattr(sections, 'education') and sections.education:
            section_count += 1
            print(f"   ✅ Education section: {len(sections.education)} entries")
            # Check for required fields in education
            for i, edu in enumerate(sections.education):
                if not hasattr(edu, 'area') or not edu.area:
                    print(f"   ⚠️  Education entry {i+1}: Missing area field")
                if not hasattr(edu, 'degree') or not edu.degree:
                    print(f"   ⚠️  Education entry {i+1}: Missing degree")
                if not hasattr(edu, 'institution') or not edu.institution:
                    print(f"   ⚠️  Education entry {i+1}: Missing institution")
        
        if hasattr(sections, 'technical_skills') and sections.technical_skills:
            section_count += 1
            print(f"   ✅ Technical Skills section: {len(sections.technical_skills)} categories")
        
        if hasattr(sections, 'certifications') and sections.certifications:
            section_count += 1
            print(f"   ✅ Certifications section: {len(sections.certifications)} items")
        
        print(f"   Total sections: {section_count}")
        
        # Design validation
        if hasattr(data_model, 'design'):
            print("4. Design settings... ✅")
        
        print()
        print("🎉 Full validation completed successfully!")
        print("📄 Your CV is ready for rendering with: rendercv render <file.yaml>")
        return True
        
    except Exception as e:
        print("❌ Validation FAILED!")
        print(f"Error: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(
        description="RenderCV YAML validation tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python validate_render_cv.py cv.yaml                    # Quick validation
  python validate_render_cv.py -d cv.yaml                 # Detailed validation
  python validate_render_cv.py -f cv.yaml                 # Full validation
  python validate_render_cv.py --mode quick cv.yaml       # Explicit quick mode
        """
    )
    
    parser.add_argument('yaml_file', help='YAML file to validate')
    parser.add_argument('-q', '--quick', action='store_true', 
                       help='Quick validation (default)')
    parser.add_argument('-d', '--detailed', action='store_true', 
                       help='Detailed validation with section info')
    parser.add_argument('-f', '--full', action='store_true', 
                       help='Full validation with all checks')
    parser.add_argument('--mode', choices=['quick', 'detailed', 'full'], 
                       help='Validation mode')
    
    args = parser.parse_args()
    
    # Determine validation mode
    if args.mode:
        mode = args.mode
    elif args.full:
        mode = 'full'
    elif args.detailed:
        mode = 'detailed'
    else:
        mode = 'quick'
    
    # Run validation
    if mode == 'quick':
        success = quick_validate(args.yaml_file)
    elif mode == 'detailed':
        success = detailed_validate(args.yaml_file)
    elif mode == 'full':
        success = full_validate(args.yaml_file)
    
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
