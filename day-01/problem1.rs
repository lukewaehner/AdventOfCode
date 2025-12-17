use std::fs;

fn convert_to_magnitude(raw: &str) -> Vec<(char, i64)> {
    raw.lines()
        .map(str::trim)
        .filter(|l| !l.is_empty())
        .map(|l| {
            let dir = l.chars().next().unwrap();
            let mag: i64 = l[1..].trim().parse().unwrap();
            (dir, mag)
        })
        .collect()
}

fn process_turn(mut current: i64, dir: char, magnitude: i64, mut zero_count: i64) -> (i64, i64) {
    if dir == 'L' {
        let mut invert_one_rot = 0i64;
        if current == 0 {
            invert_one_rot = -1;
        }

        current = current - magnitude;

        if current < 0 {
            let q = floor_div(current - 1, 100);
            zero_count += q.abs() + invert_one_rot;
            current = mod_floor(current, 100);
        } else if current == 0 {
            zero_count += 1;
        }
    } else if dir == 'R' {
        current = current + magnitude;
        if current >= 100 {
            zero_count += current / 100;
            current %= 100;
        }
    } else {
        panic!("Invalid direction: {}", dir);
    }

    (current, zero_count)
}

fn floor_div(a: i64, b: i64) -> i64 {
    assert!(b > 0);
    if a >= 0 { a / b } else { -(((-a) + b - 1) / b) }
}

fn mod_floor(a: i64, b: i64) -> i64 {
    assert!(b > 0);
    let m = a % b;
    if m < 0 { m + b } else { m }
}

fn solve(input: &str) -> i64 {
    let magnitudes = convert_to_magnitude(input);
    let mut zero_count: i64 = 0;
    let mut current: i64 = 50;

    for (dir, magnitude) in magnitudes {
        let (next_current, next_zero) = process_turn(current, dir, magnitude, zero_count);
        current = next_current;
        zero_count = next_zero;
    }

    zero_count
}

fn main() {
    let input = fs::read_to_string("input.txt").expect("failed to read input.txt");
    let ans = solve(&input);
    println!("{}", ans);
}
